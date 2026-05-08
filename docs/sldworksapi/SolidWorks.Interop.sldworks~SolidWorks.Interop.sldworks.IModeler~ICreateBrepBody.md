# ICreateBrepBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody`

Obsolete. Superseded by IModeler::ICreateBrepBody3.
Obsolete. Superseded by [IModeler::ICreateBrepBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBrepBody( _
   ByVal Type As System.Integer, _
   ByVal NTopologies As System.Integer, _
   ByRef Topologies As System.Integer, _
   ByRef EdgeTolArray As System.Double, _
   ByRef VertexTolArray As System.Double, _
   ByRef PointArray As System.Double, _
   ByRef CurveArray As Curve, _
   ByRef SurfaceArray As Surface, _
   ByVal NRelations As System.Integer, _
   ByRef Parents As System.Integer, _
   ByRef Children As System.Integer, _
   ByRef Senses As System.Integer _
) As Body
```

```

Dim instance As IModeler
Dim Type As System.Integer
Dim NTopologies As System.Integer
Dim Topologies As System.Integer
Dim EdgeTolArray As System.Double
Dim VertexTolArray As System.Double
Dim PointArray As System.Double
Dim CurveArray As Curve
Dim SurfaceArray As Surface
Dim NRelations As System.Integer
Dim Parents As System.Integer
Dim Children As System.Integer
Dim Senses As System.Integer
Dim value As Body
 
value = instance.ICreateBrepBody(Type, NTopologies, Topologies, EdgeTolArray, VertexTolArray, PointArray, CurveArray, SurfaceArray, NRelations, Parents, Children, Senses)
```

```

Body ICreateBrepBody( 
   System.int Type,
   System.int NTopologies,
   ref System.int Topologies,
   ref System.double EdgeTolArray,
   ref System.double VertexTolArray,
   ref System.double PointArray,
   ref Curve CurveArray,
   ref Surface SurfaceArray,
   System.int NRelations,
   ref System.int Parents,
   ref System.int Children,
   ref System.int Senses
)
```

```

Body^ ICreateBrepBody( 
   System.int Type,
   System.int NTopologies,
   System.int% Topologies,
   System.double% EdgeTolArray,
   System.double% VertexTolArray,
   System.double% PointArray,
   Curve^% CurveArray,
   Surface^% SurfaceArray,
   System.int NRelations,
   System.int% Parents,
   System.int% Children,
   System.int% Senses
) 
```

#### Parameters

*Type*

*NTopologies*

*Topologies*

*EdgeTolArray*

*VertexTolArray*

*PointArray*

*CurveArray*

*SurfaceArray*

*NRelations*

*Parents*

*Children*

*Senses*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
