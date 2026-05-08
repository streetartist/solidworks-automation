# AddPathLengthDim Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddPathLengthDim`

Inserts a path length dimension at the specified coordinates for a selected path.
Inserts a path length dimension at the specified coordinates for a selected path.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddPathLengthDim( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object
 
value = instance.AddPathLengthDim(X, Y, Z)
```

```

System.object AddPathLengthDim( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.Object^ AddPathLengthDim( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X coordinate of display dimension

*Y*
:   Y coordinate of display dimension

*Z*
:   Z coordinate of display dimension

#### Return Value

[IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)

Remarks

Before calling this method to create a path length dimension:

| If a path... | Then... |
| --- | --- |
| Exists | Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select one sketch segment on the existing path. |
| Does not exist | 1. Call IModelDocExtension::SelectByID2 to select two or more sketch segments that are end-to-end coincident and form a single chain. 2. Call [ISketchManager::MakeSketchChain](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchChain.md) to create a path with the selected sketch segments. 3. Call IModelDocExtension::SelectByID2 to select one sketch segment on the path. |

Example

[Create Path Length Dimension (VBA)](Create_Path_Length_Dimension_Example_VB.htm)  
[Create Path Length Dimension (VB.NET)](Create_Path_Length_Dimension_Example_VBNET.htm)  
[Create Path Length Dimension (C#)](Create_Path_Length_Dimension_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
