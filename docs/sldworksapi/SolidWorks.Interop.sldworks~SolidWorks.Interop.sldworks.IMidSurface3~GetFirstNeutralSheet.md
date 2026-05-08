# GetFirstNeutralSheet Method (IMidSurface3)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstNeutralSheet`

Gets the first reference surface in this midsurface }}-->feature.
Gets the first reference surface in this midsurface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstNeutralSheet() As System.Object
```

```

Dim instance As IMidSurface3
Dim value As System.Object
 
value = instance.GetFirstNeutralSheet()
```

```

System.object GetFirstNeutralSheet()
```

```

System.Object^ GetFirstNeutralSheet(); 
```

#### Return Value

First reference surface sheet [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) in this midsurface feature

Remarks

Each reference surface in the midsurface feature is considered to be a sheet body. If the reference surfaces are sewn together during the creation of the midsurface feature ([IModelDoc2::InsertMidSurfaceExt](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertMidSurfaceExt.md)), then the midsurface feature contains only one reference surface sheet body.

The sheet body returned from this method has the normal topology that you would expect to find on a body (for example, faces, edges, and so on). See the [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) object for methods that provide access to this topology.

Call [IMidSurface3::GetNextNeutralSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextNeutralSheet.md) to get the next reference surface in this midsurface feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.md)  
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.md)  
[IMidSurface3::IGetNextNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextNeutralSheet.md)  
[IMidSurface3::GetNeutralSheetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNeutralSheetCount.md)
