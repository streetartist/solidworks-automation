# GetLineInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetLineInfo`

Gets the vertices of the section line.
Gets the vertices of the section line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLineInfo() As System.Object
```

```

Dim instance As IDrSection
Dim value As System.Object
 
value = instance.GetLineInfo()
```

```

System.object GetLineInfo()
```

```

System.Object^ GetLineInfo(); 
```

#### Return Value

Array (see **Remarks**)

Remarks

This method returns an array that consists of several coordinate pairs. The number of coordinate pairs is determined by the number of line segments in the section line.

These values are the same as some of the information in the array returned by the[IView::GetSectionLineInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineInfo2.md). The line segment information in that array also contains the line style. The array returned by this method does not contain that information because it is a document-level setting, and cannot be controlled per section line. Use [IModelDocExtension::GetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.md) or [IModelDocExtension::SetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceInteger.md) with swLineFontSectionLineStyle to get or set that value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::SetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetLineInfo.md)  
[IDrSection::IGetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetLineInfo.md)  
[IDrSection::SetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetLineInfo.md)  
[IView::GetSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLines.md)  
[IView::EnumSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines.md)  
[IDrSection::IGetLineSegmentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetLineSegmentCount.md)  
[IView::GetSectionLineInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineInfo2.md)  
[IView::IGetSectionLineInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLineInfo2.md)
