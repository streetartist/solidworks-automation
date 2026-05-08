# GetBodyOutline2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetBodyOutline2`

Gets the curves that form the outline of a body.
Gets the curves that form the outline of a body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBodyOutline2( _
   ByVal BodyList As System.Object, _
   ByVal Direction As MathVector, _
   ByVal Tolerance As System.Double, _
   ByVal ProjectOnPlane As System.Boolean, _
   ByRef Curves As System.Object, _
   ByRef TopolEntities As System.Object, _
   ByRef Outline As System.Object _
) As System.Integer
```

```

Dim instance As IModeler
Dim BodyList As System.Object
Dim Direction As MathVector
Dim Tolerance As System.Double
Dim ProjectOnPlane As System.Boolean
Dim Curves As System.Object
Dim TopolEntities As System.Object
Dim Outline As System.Object
Dim value As System.Integer
 
value = instance.GetBodyOutline2(BodyList, Direction, Tolerance, ProjectOnPlane, Curves, TopolEntities, Outline)
```

```

System.int GetBodyOutline2( 
   System.object BodyList,
   MathVector Direction,
   System.double Tolerance,
   System.bool ProjectOnPlane,
   out System.object Curves,
   out System.object TopolEntities,
   out System.object Outline
)
```

```

System.int GetBodyOutline2( 
   System.Object^ BodyList,
   MathVector^ Direction,
   System.double Tolerance,
   System.bool ProjectOnPlane,
   [Out] System.Object^ Curves,
   [Out] System.Object^ TopolEntities,
   [Out] System.Object^ Outline
) 
```

#### Parameters

*BodyList*
:   Array of bodies

*Direction*
:   [IMathVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) direction of view

*Tolerance*
:   Tolerance (Parasolid default 0.00001)

*ProjectOnPlane*
:   True to project the curves onto a plane, false to not (see **Remarks**)

*Curves*
:   Array of 3D trimmed curves that form the outline

*TopolEntities*
:   Array of topological entities associated with the outline

*Outline*
:   Array of integers indicating which curves belong to which outline

#### Return Value

Number of curves that form the outline

Remarks

When rendered, the array of curves returned in Curves might not display as a continuous outline of the body.

To close gaps:

1. Call this method with ProjectOnPlane = true.
2. Post-process the array of curves returned in Curves to interpolate the end points of each curve to generate a continuous outline of the body. See the **Get Body Outline** examples.

Example

[Get Curves that Form Outline of Bodies (VBA)](Get_Curves_that_Form_Outline_of_Bodies_Example_VB.htm)  
[Get Body Outline (VBA)](Get_Body_Outline_Example_VB.htm)  
[Get Body Outline (VB.NET)](Get_Body_Outline_Example_VBNET.htm)  
[Get Body Outline (C#)](Get_Body_Outline_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
