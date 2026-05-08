# GeneralTopology Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GeneralTopology`

Gets or sets the Parasolid option to create general (non-manifold) bodies.
Gets or sets the Parasolid option to create general (non-manifold) bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GeneralTopology As System.Boolean
```

```

Dim instance As IModeler
Dim value As System.Boolean
 
instance.GeneralTopology = value
 
value = instance.GeneralTopology
```

```

System.bool GeneralTopology {get; set;}
```

```

property System.bool GeneralTopology {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to create general bodies, false to not

Remarks

SOLIDWORKS expects this property be false because SOLIDWORKS does not support the creation of general bodies. If you set this property to True, then set it back to false as soon as your intended operations complete.

To tessellate a general body, set [ITesssellation::MatchType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~MatchType.md) to swTesselationMatchFacetGeometry, which sets the Parasolid facet match to clipping facet boundaries to a common edge

Example

[Create and Convert Non-manifold Bodies (C#)](Create_and_Convert_Non-manifold_Bodies_Example_CSharp.htm)  
[Create and Convert Non-manifold Bodies (VB.NET)](Create_and_Convert_Non-manifold_Bodies_Example_VBNET.htm)  
[Create and Convert Non-manifold Bodies (VBA)](Create_and_Convert_Non-manifold_Bodies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::GetManifoldBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetManifoldBodiesCount.md)  
[IModeler::IMakeManifoldBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IMakeManifoldBodies.md)  
[IModeler::MakeManifoldBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~MakeManifoldBodies.md)
