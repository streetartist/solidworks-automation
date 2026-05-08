# CreateBrepBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody`

Obsolete. Superseded by IModeler::CreateBrepBody3.
Obsolete. Superseded by [IModeler::CreateBrepBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBrepBody( _
   ByVal Type As System.Integer, _
   ByVal NTopologies As System.Integer, _
   ByVal Topologies As System.Object, _
   ByVal EdgeToleranceArray As System.Object, _
   ByVal VertexToleranceArray As System.Object, _
   ByVal PointArray As System.Object, _
   ByVal CurveArray As System.Object, _
   ByVal SurfaceArray As System.Object, _
   ByVal NRelations As System.Integer, _
   ByVal Parents As System.Object, _
   ByVal Children As System.Object, _
   ByVal Senses As System.Object _
) As System.Object
```

```

Dim instance As IModeler
Dim Type As System.Integer
Dim NTopologies As System.Integer
Dim Topologies As System.Object
Dim EdgeToleranceArray As System.Object
Dim VertexToleranceArray As System.Object
Dim PointArray As System.Object
Dim CurveArray As System.Object
Dim SurfaceArray As System.Object
Dim NRelations As System.Integer
Dim Parents As System.Object
Dim Children As System.Object
Dim Senses As System.Object
Dim value As System.Object
 
value = instance.CreateBrepBody(Type, NTopologies, Topologies, EdgeToleranceArray, VertexToleranceArray, PointArray, CurveArray, SurfaceArray, NRelations, Parents, Children, Senses)
```

```

System.object CreateBrepBody( 
   System.int Type,
   System.int NTopologies,
   System.object Topologies,
   System.object EdgeToleranceArray,
   System.object VertexToleranceArray,
   System.object PointArray,
   System.object CurveArray,
   System.object SurfaceArray,
   System.int NRelations,
   System.object Parents,
   System.object Children,
   System.object Senses
)
```

```

System.Object^ CreateBrepBody( 
   System.int Type,
   System.int NTopologies,
   System.Object^ Topologies,
   System.Object^ EdgeToleranceArray,
   System.Object^ VertexToleranceArray,
   System.Object^ PointArray,
   System.Object^ CurveArray,
   System.Object^ SurfaceArray,
   System.int NRelations,
   System.Object^ Parents,
   System.Object^ Children,
   System.Object^ Senses
) 
```

#### Parameters

*Type*

*NTopologies*

*Topologies*

*EdgeToleranceArray*

*VertexToleranceArray*

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
