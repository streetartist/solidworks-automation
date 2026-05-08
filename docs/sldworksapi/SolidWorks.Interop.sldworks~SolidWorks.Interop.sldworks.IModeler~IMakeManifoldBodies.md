# IMakeManifoldBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IMakeManifoldBodies`

Creates manifold bodies from the specified non-manifold body.
Creates manifold bodies from the specified non-manifold body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IMakeManifoldBodies( _
   ByVal NonManifoldIn As Body2, _
   ByVal Count As System.Integer _
) As Body2
```

```

Dim instance As IModeler
Dim NonManifoldIn As Body2
Dim Count As System.Integer
Dim value As Body2
 
value = instance.IMakeManifoldBodies(NonManifoldIn, Count)
```

```

Body2 IMakeManifoldBodies( 
   Body2 NonManifoldIn,
   System.int Count
)
```

```

Body2^ IMakeManifoldBodies( 
   Body2^ NonManifoldIn,
   System.int Count
) 
```

#### Parameters

*NonManifoldIn*
:   Non-manifold [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

*Count*
:   Number of manifold bodies

#### Return Value

[Manifold bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

Call [IModeler::GetManifoldBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetManifoldBodiesCount.md) before calling this method to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::MakeManifoldBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~MakeManifoldBodies.md)  
[IModeler::GeneralTopology Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GeneralTopology.md)
