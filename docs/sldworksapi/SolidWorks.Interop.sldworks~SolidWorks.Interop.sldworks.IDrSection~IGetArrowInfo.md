# IGetArrowInfo Method (IDrSection)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetArrowInfo`

Gets the position of the arrows for this section line.
Gets the position of the arrows for this section line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetArrowInfo() As System.Double
```

```

Dim instance As IDrSection
Dim value As System.Double
 
value = instance.IGetArrowInfo()
```

```

System.double IGetArrowInfo()
```

```

System.double IGetArrowInfo(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of 3 doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The section line in a drawing view has arrows at each end of the line. This method returns an array that consists of 12 doubles, the (X, Y, Z) of the start and end point of one arrow followed by the (X, Y, Z) of the start and end point of the other arrow.

These values are the same as some of the information in the array returned by View::GetSectionLineInfo. The arrow information in that array also contains the arrow width, height and style. That information is not included in the array returned by this method, but you can get it from the document preference settings because these values are controlled only at the document level, not on an individual section line basis.

See:

- [IModelDocExtension::GetUserPreferenceDouble](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.md) with swDetailingSectionArrowHeight, swDetailingSectionArrowWidth, or swDetailingSectionArrowLength
- [IModelDocExtension::GetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.md) with swDetailingArrowStyleForDimensions

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::GetArrowInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetArrowInfo.md)
