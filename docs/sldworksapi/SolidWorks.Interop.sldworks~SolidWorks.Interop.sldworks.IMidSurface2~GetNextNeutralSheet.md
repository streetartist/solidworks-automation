# GetNextNeutralSheet Method (IMidSurface2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextNeutralSheet`

Obsolete. Superseded by IMidSurface3::GetNextNeutralSheet.
Obsolete. Superseded by [IMidSurface3::GetNextNeutralSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextNeutralSheet.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNextNeutralSheet() As System.Object
```

```

Dim instance As IMidSurface2
Dim value As System.Object
 
value = instance.GetNextNeutralSheet()
```

```

System.object GetNextNeutralSheet()
```

```

System.Object^ GetNextNeutralSheet(); 
```

#### Return Value

Next reference surface sheet [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) in this midsurface feature

Remarks

Each reference surface in the midsurface feature is considered a sheet body. If the reference surfaces are sewn together during the creation of the midsurface feature ([IModelDoc2::InsertMidSurfaceExt](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertMidSurfaceExt.md)), then the midsurface feature contains only one reference surface sheet body. If this is the case, then this method returns NULL. Use [IMidSurface2::GetFirstNeutralSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNeutralSheetCount.md) to get the first and only reference surface sheet body.

The sheet body returned from this method has the normal topology that you would expect to find on a body (for example, faces, edges, and so on). See the [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) object for methods that provide access to this topology.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.md)  
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.md)  
[IMidSurface2::IGetNextNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextNeutralSheet.md)  
[IMidSurface2::IGetFirstNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstNeutralSheet.md)  
[IMidSurface2::GetNeutralSheetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNeutralSheetCount.md)
