# EnumSectionLines Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines`

Obsolete. Superseded by IView::EnumSectionLines2.
Obsolete. Superseded by [IView::EnumSectionLines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumSectionLines() As EnumDrSections
```

```

Dim instance As IView
Dim value As EnumDrSections
 
value = instance.EnumSectionLines()
```

```

EnumDrSections EnumSectionLines()
```

```

EnumDrSections^ EnumSectionLines(); 
```

#### Return Value

[Section lines enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections.md)

Remarks

This method returns the section lines regardless of whether the view is visible. If the view is hidden, then the section lines are still returned.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetSectionLineCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineCount2.md)  
[IView::GetSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLines.md)  
[IView::GetSectionLineStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineStrings.md)
