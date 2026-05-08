# GetArrowInfo Method (IDetailCircle)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetArrowInfo`

Gets the position of the arrows for this detail circle.
Gets the position of the arrows for this detail circle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArrowInfo() As System.Object
```

```

Dim instance As IDetailCircle
Dim value As System.Object
 
value = instance.GetArrowInfo()
```

```

System.object GetArrowInfo()
```

```

System.Object^ GetArrowInfo(); 
```

#### Return Value

Array containing the arrow position information

Remarks

The section line in a drawing view has arrows at each end of the line. This method returns an array that contains 12 doubles, the (X, Y, Z) of the start and end point of one arrow, followed by the (X, Y, Z) of the start and end point of the other arrow.

These values match some of the information in the array returned by [IView::GetSectionLineInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineInfo2.md) and [IViewIGetSectionLineInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLineInfo2.md); the arrow information near the middle of the array. The arrow information in that array also contains the arrow width, height, and style, which is not in the array returned by this method. To get this information using document preference settings, use [IModelDocExtension::GetUserPreferenceDouble](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.md) with swDetailingSectionArrowHeight, swDetailingSectionArrowWidth, or swDetailingSectionArrowLength, and  [IModelDocExtension::GetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.md) with swDetailingArrowStyleForDimensions.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)  
[IDetailCircle::IGetArrowInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~IGetArrowInfo.md)
