# GetRouteManager Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetRouteManager`

Gets the SOLIDWORKS Routing API.
Gets the SOLIDWORKS Routing API.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRouteManager() As System.Object
```

```

Dim instance As IAssemblyDoc
Dim value As System.Object
 
value = instance.GetRouteManager()
```

```

System.object GetRouteManager()
```

```

System.Object^ GetRouteManager(); 
```

#### Return Value

SOLIDWORKS Routing API

Example

[Create Auto Route (VBA)](Create_Auto_Route_Example_VB.htm)  
[Create Auto Route (VB.NET)](Create_Auto_Route_Example_VBNET.htm)  
[Create Auto Route (C#)](Create_Auto_Route_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::IsRouteAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IsRouteAssembly.md)  
[IModelDoc2::EditRoute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRoute.md)  
[IModelDoc2::InsertRoutePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRoutePoint.md)  
[IFeatureManager::InsertConnectionPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertConnectionPoint.md)
