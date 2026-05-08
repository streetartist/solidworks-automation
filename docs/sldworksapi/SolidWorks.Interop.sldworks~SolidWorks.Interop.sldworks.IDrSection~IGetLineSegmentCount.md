# IGetLineSegmentCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetLineSegmentCount`

Gets the number of line segments making up this section line.
Gets the number of line segments making up this section line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetLineSegmentCount() As System.Integer
```

```

Dim instance As IDrSection
Dim value As System.Integer
 
value = instance.IGetLineSegmentCount()
```

```

System.int IGetLineSegmentCount()
```

```

System.int IGetLineSegmentCount(); 
```

#### Return Value

Number of line segments in this section line

Remarks

Use this method to determine the size of the array you need to allocate for the output of [IDrSection::IGetLineInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetLineInfo.md). The size of the array to allocate is (6 \* the value returned by this method).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::GetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetLineInfo.md)  
[IDrSection::ISetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ISetLineInfo.md)  
[IDrSection::SetLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetLineInfo.md)  
[IView::GetSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLines.md)  
[IView::EnumSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines.md)
