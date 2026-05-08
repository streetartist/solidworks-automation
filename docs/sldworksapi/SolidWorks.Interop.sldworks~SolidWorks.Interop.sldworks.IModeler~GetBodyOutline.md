# GetBodyOutline Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetBodyOutline`

Obsolete. Superseded by IModeler::GetBodyOutline2.
Obsolete. Superseded by [IModeler::GetBodyOutline2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetBodyOutline2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBodyOutline( _
   ByVal BodyVar As System.Object, _
   ByVal Direction As MathVector, _
   ByVal Tolerance As System.Double, _
   ByRef CurvesOut As System.Object, _
   ByRef TopolEntities As System.Object, _
   ByRef Outline As System.Object _
) As System.Integer
```

```

Dim instance As IModeler
Dim BodyVar As System.Object
Dim Direction As MathVector
Dim Tolerance As System.Double
Dim CurvesOut As System.Object
Dim TopolEntities As System.Object
Dim Outline As System.Object
Dim value As System.Integer
 
value = instance.GetBodyOutline(BodyVar, Direction, Tolerance, CurvesOut, TopolEntities, Outline)
```

```

System.int GetBodyOutline( 
   System.object BodyVar,
   MathVector Direction,
   System.double Tolerance,
   out System.object CurvesOut,
   out System.object TopolEntities,
   out System.object Outline
)
```

```

System.int GetBodyOutline( 
   System.Object^ BodyVar,
   MathVector^ Direction,
   System.double Tolerance,
   [Out] System.Object^ CurvesOut,
   [Out] System.Object^ TopolEntities,
   [Out] System.Object^ Outline
) 
```

#### Parameters

*BodyVar*
:   Array of bodies

*Direction*
:   Direction of view

*Tolerance*
:   Tolerance (Parasolid default 0.00001)

*CurvesOut*
:   Array of 3D trimmed curves that form the outline

*TopolEntities*
:   Array of topological entities associated with the outline

*Outline*
:   Array of integers indicating which curves belong to which outline

#### Return Value

Number of curves that form the outline of a body

Remarks

See Parasolid's documentation of PK\_BODY\_make\_curves\_outline for more information about the output.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
