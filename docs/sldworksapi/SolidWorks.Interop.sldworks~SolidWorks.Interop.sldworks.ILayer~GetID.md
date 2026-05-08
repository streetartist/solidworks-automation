# GetID Method (ILayer)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~GetID`

Gets the layer ID for this layer.
Gets the layer ID for this layer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetID() As System.Integer
```

```

Dim instance As ILayer
Dim value As System.Integer
 
value = instance.GetID()
```

```

System.int GetID()
```

```

System.int GetID(); 
```

#### Return Value

Layer ID for this layer

Remarks

A layer ID:

- is unique within the drawing.
- is persistent across SOLIDWORKS sessions and never changes, even if you [change the name of the layer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Name.md).
- can be used to identify a specific layer when multiple layers exist in a drawing.
- cannot be assigned by applications or users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm). You can get a layer using its persistent reference ID, but you cannot get a layer using this method.

Example

[Get Layers (C#)](Get_Layers_Example_CSharp.htm)  
[Get Layers (VB.NET)](Get_Layers_Example_VBNET.htm)  
[Get Layers (VBA)](Get_Layers_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md)  
[ILayer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer_members.md)
