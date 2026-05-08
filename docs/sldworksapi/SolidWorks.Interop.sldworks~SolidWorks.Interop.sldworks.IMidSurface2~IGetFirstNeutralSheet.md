# IGetFirstNeutralSheet Method (IMidSurface2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstNeutralSheet`

Obsolete. Superseded by IMidSurface3::IGetFirstNeutralSheet.
Obsolete. Superseded by [IMidSurface3::IGetFirstNeutralSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetFirstNeutralSheet.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFirstNeutralSheet() As Body2
```

```

Dim instance As IMidSurface2
Dim value As Body2
 
value = instance.IGetFirstNeutralSheet()
```

```

Body2 IGetFirstNeutralSheet()
```

```

Body2^ IGetFirstNeutralSheet(); 
```

#### Return Value

First reference surface sheet [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) in this midsurface feature

Remarks

Each reference surface in the midsurface feature is considered to be a sheet body. If the reference surfaces are sewn together during the creation of the midsurface feature ([IModelDoc2::IInsertMidSurfaceExt](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertMidSurfaceExt.md)), then the midsurface feature contains only one reference surface sheet body.

The sheet body returned from this method has the normal topology that you would expect to find on a body (for example, faces, edges, and so on). See the [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) object for methods that provide access to this topology.

Call [IMidSurface2::IGetNextNeutralSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextNeutralSheet.md) to get the next reference surface in this midsurface feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.md)  
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.md)  
[IMidSurface2::GetFirstNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFirstNeutralSheet.md)  
[IMidSurface2::GetNextNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextNeutralSheet.md)  
[IMidSurface2::GetNeutralSheetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNeutralSheetCount.md)
