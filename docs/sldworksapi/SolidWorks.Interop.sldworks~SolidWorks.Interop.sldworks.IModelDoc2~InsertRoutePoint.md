# InsertRoutePoint Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRoutePoint`

Adds a route point based on the selected point.
Adds a route point based on the selected point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertRoutePoint() 
```

```

Dim instance As IModelDoc2
 
instance.InsertRoutePoint()
```

```

void InsertRoutePoint()
```

```

void InsertRoutePoint(); 
```

Remarks

If the selection set is not complete, then the Insert Route Point dialog is displayed.

The route point is the point on the fitting that aligns with the sketch point when the fitting is inserted.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::EditRoute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRoute.md)  
[IAssemblyDoc::GetRouteManager Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetRouteManager.md)  
[IAssemblyDoc::IsRouteAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IsRouteAssembly.md)  
[IFeatureManager::InsertConnectionPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertConnectionPoint.md)
