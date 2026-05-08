# GetCurrentLayer Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetCurrentLayer`

Gets the name of the current (active) layer in this drawing document.
Gets the name of the current (active) layer in this drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurrentLayer() As System.String
```

```

Dim instance As ILayerMgr
Dim value As System.String
 
value = instance.GetCurrentLayer()
```

```

System.string GetCurrentLayer()
```

```

System.String^ GetCurrentLayer(); 
```

#### Return Value

Name of the active layer

Remarks

If an empty string is returned, then there is no active layer and -None- is displayed in the Layer toolbar.

To access information about a layer, get the [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object by passing the layer name to [ILayerMgr::GetLayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayer.md).

To change the currently active layer, use [ILayerMgr::SetCurrentLayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~SetCurrentLayer.md).

Example

[Get Layers (VBA)](Get_Layers_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.md)  
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.md)  
[ILayerMgr::SetCurrentLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~SetCurrentLayer.md)
