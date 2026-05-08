# MakeManifoldBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~MakeManifoldBodies`

Creates manifold bodies from the specified non-manifold body.
Creates manifold bodies from the specified non-manifold body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeManifoldBodies( _
   ByVal NonManifoldIn As Body2 _
) As System.Object
```

```

Dim instance As IModeler
Dim NonManifoldIn As Body2
Dim value As System.Object
 
value = instance.MakeManifoldBodies(NonManifoldIn)
```

```

System.object MakeManifoldBodies( 
   Body2 NonManifoldIn
)
```

```

System.Object^ MakeManifoldBodies( 
   Body2^ NonManifoldIn
) 
```

#### Parameters

*NonManifoldIn*
:   Non-manifold [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

#### Return Value

[Manifold bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

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
[IModeler::IMakeManifoldBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IMakeManifoldBodies.md)  
[IModeler::GeneralTopology Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GeneralTopology.md)
