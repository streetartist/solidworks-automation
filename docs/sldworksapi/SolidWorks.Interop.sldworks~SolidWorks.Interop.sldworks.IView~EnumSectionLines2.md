# EnumSectionLines2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines2`

Gets the section lines enumeration in the view.
Gets the section lines enumeration in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumSectionLines2( _
   ByVal IgnoreSuppressed As System.Boolean _
) As EnumDrSections
```

```

Dim instance As IView
Dim IgnoreSuppressed As System.Boolean
Dim value As EnumDrSections
 
value = instance.EnumSectionLines2(IgnoreSuppressed)
```

```

EnumDrSections EnumSectionLines2( 
   System.bool IgnoreSuppressed
)
```

```

EnumDrSections^ EnumSectionLines2( 
   System.bool IgnoreSuppressed
) 
```

#### Parameters

*IgnoreSuppressed*
:   True to ignore suppressed section lines, false to include them

#### Return Value

[Section lines enumeration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections.md)

Remarks

This method returns section lines whether the view is visible or not. If the view is hidden, then the section lines are still returned.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetSectionLineCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineCount2.md)  
[IView::GetSectionLines Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLines.md)  
[IView::GetSectionLineStrings Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineStrings.md)
