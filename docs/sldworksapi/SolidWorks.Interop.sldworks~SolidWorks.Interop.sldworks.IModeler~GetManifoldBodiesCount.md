# GetManifoldBodiesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetManifoldBodiesCount`

Gets the number of manifold bodies created from the specified non-manifold body.
Gets the number of manifold bodies created from the specified non-manifold body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetManifoldBodiesCount( _
   ByVal NonManifoldIn As Body2 _
) As System.Integer
```

```

Dim instance As IModeler
Dim NonManifoldIn As Body2
Dim value As System.Integer
 
value = instance.GetManifoldBodiesCount(NonManifoldIn)
```

```

System.int GetManifoldBodiesCount( 
   Body2 NonManifoldIn
)
```

```

System.int GetManifoldBodiesCount( 
   Body2^ NonManifoldIn
) 
```

#### Parameters

*NonManifoldIn*
:   Non-manifold [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

#### Return Value

Number of manifold bodies

Remarks

Call this method before calling [IModeler::IMakeManifoldBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IMakeManifoldBodies.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::GeneralTopology Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GeneralTopology.md)  
[IModeler::MakeManifoldBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~MakeManifoldBodies.md)
