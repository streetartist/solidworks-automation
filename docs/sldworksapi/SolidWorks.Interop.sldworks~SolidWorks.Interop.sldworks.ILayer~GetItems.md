# GetItems Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~GetItems`

Gets the items on this layer.
Gets the items on this layer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetItems( _
   ByVal ItemType As System.Integer _
) As System.Object
```

```

Dim instance As ILayer
Dim ItemType As System.Integer
Dim value As System.Object
 
value = instance.GetItems(ItemType)
```

```

System.object GetItems( 
   System.int ItemType
)
```

```

System.Object^ GetItems( 
   System.int ItemType
) 
```

#### Parameters

*ItemType*
:   Items to get as defined in [swLayerItemsOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLayerItemsOption_e.html)

#### Return Value

Array of layer items

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md)  
[ILayer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer_members.md)
