# InsertRadiateSurface Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRadiateSurface`

Creates a radiate surface based on the selections.
Creates a radiate surface based on the selections.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertRadiateSurface( _
   ByVal Distance As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal TangentPropagate As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim Distance As System.Double
Dim FlipDir As System.Boolean
Dim TangentPropagate As System.Boolean
 
instance.InsertRadiateSurface(Distance, FlipDir, TangentPropagate)
```

```

void InsertRadiateSurface( 
   System.double Distance,
   System.bool FlipDir,
   System.bool TangentPropagate
)
```

```

void InsertRadiateSurface( 
   System.double Distance,
   System.bool FlipDir,
   System.bool TangentPropagate
) 
```

#### Parameters

*Distance*
:   Distance to extend the surface

*FlipDir*
:   True to flip the direction; by default the direction is out from the center of the face

*TangentPropagate*
:   True to propagate the surface along tangent faces, false limits the surface to the selected face

Remarks

Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select

- Reference direction using Mark = 1.
- Radiate entities using Mark = 2.

See the SOLIDWORKS Help for information about what entities are valid for selection.

Example

[Create Radiate Surface Feature (VBA)](Get_Radiate_Surface_Data_Example_VB.htm)  
[Create Radiate Surface Feature (VB.NET)](Create_Radiate_Surface_Example_VBNET.htm)  
[Create Radiate Surface Feature (C#)](Create_Radiate_Surface_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[ISurfaceRadiateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.md)
