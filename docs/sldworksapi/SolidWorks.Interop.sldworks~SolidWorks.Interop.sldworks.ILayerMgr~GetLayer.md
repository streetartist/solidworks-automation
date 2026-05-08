# GetLayer Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayer`

Gets the specified layer in this drawing document.
Gets the specified layer in this drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLayer( _
   ByVal NameIn As System.String _
) As System.Object
```

```

Dim instance As ILayerMgr
Dim NameIn As System.String
Dim value As System.Object
 
value = instance.GetLayer(NameIn)
```

```

System.object GetLayer( 
   System.string NameIn
)
```

```

System.Object^ GetLayer( 
   System.String^ NameIn
) 
```

#### Parameters

*NameIn*
:   Layer name

#### Return Value

Layer

Remarks

You can get the layer name by calling [ILayerMgr::GetCurrentLayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetCurrentLayer.md), create a new layer calling [ILayerMgr::AddLayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~AddLayer.md), or obtain a list of layer names by calling [ILayerMgr::GetLayerList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerList.md).

Example

[Determine If Layer Is Visible (VBA)](Determine_if_Layer_is_Visible_Example_VB.htm)  
[Get Layers (C#)](Get_Layers_Example_CSharp.htm)  
[Get Layers (VB.NET)](Get_Layers_Example_VBNET.htm)  
[Get Layers (VBA)](Get_Layers_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.md)  
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.md)  
[ILayerMgr::IGetLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayer.md)
