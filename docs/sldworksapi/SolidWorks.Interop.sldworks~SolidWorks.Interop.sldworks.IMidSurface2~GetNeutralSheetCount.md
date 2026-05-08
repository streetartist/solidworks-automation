# GetNeutralSheetCount Method (IMidSurface2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNeutralSheetCount`

Obsolete. Superseded by IMidSurface3::GetNeutralSheetCount.
Obsolete. Superseded by [IMidSurface3::GetNeutralSheetCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNeutralSheetCount.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNeutralSheetCount() As System.Integer
```

```

Dim instance As IMidSurface2
Dim value As System.Integer
 
value = instance.GetNeutralSheetCount()
```

```

System.int GetNeutralSheetCount()
```

```

System.int GetNeutralSheetCount(); 
```

#### Return Value

Number of reference surface sheet bodies found in this midsurface feature

Remarks

Each reference surface in the midsurface feature is considered to be a sheet body. If the reference surfaces are sewn together during the creation of our midsurface feature ([IModelDoc2::InsertMidSurfaceExt](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertMidSurfaceExt.md) or [IModelDoc2::IInsertMidSurfaceExt](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertMidSurfaceExt.md)), then the midsurface feature contains only one reference surface sheet body.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.md)  
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.md)  
[IMidSurface2::IGetFirstNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstNeutralSheet.md)  
[IMidSurface2::GetFirstNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFirstNeutralSheet.md)  
[IMidSurface2::IGetNextNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextNeutralSheet.md)  
[IMidSurface2::GetNextNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextNeutralSheet.md)
