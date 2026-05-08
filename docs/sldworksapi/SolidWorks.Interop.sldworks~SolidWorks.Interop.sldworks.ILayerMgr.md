# ILayerMgr Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr`

Allows you to manage a drawing document's layers.
Allows you to manage a drawing document's layers.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ILayerMgr 
```

```

Dim instance As ILayerMgr
```

```

public interface ILayerMgr 
```

```

public interface class ILayerMgr 
```

Remarks

Each drawing document has its own ILayerMgr object and its own [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) objects. The ILayerMgr interface provides functions that allow you to manipulate and work with individual layers. This includes adding layers, setting the current layer, obtaining specific layers, etc.

Layers are only supported in SOLIDWORKS drawing documents.

Example

[Get Layers (C#)](Get_Layers_Example_CSharp.htm)  
[Get Layers (VB.NET)](Get_Layers_Example_VBNET.htm)  
[Get Layers (VBA)](Get_Layers_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)
