# GetBendLineValues2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBendLineValues2`

Gets the values of a bend line note.
Gets the values of a bend line note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBendLineValues2( _
   ByRef Up As System.Boolean, _
   ByRef Angle As System.Double, _
   ByRef Radius As System.Double, _
   ByRef Points As System.Object _
) As System.Boolean
```

```

Dim instance As INote
Dim Up As System.Boolean
Dim Angle As System.Double
Dim Radius As System.Double
Dim Points As System.Object
Dim value As System.Boolean
 
value = instance.GetBendLineValues2(Up, Angle, Radius, Points)
```

```

System.bool GetBendLineValues2( 
   out System.bool Up,
   out System.double Angle,
   out System.double Radius,
   out System.object Points
)
```

```

System.bool GetBendLineValues2( 
   [Out] System.bool Up,
   [Out] System.double Angle,
   [Out] System.double Radius,
   [Out] System.Object^ Points
) 
```

#### Parameters

*Up*
:   True if the bend is up, false if the bend is down

*Angle*
:   Angle of the bend

*Radius*
:   Radius of the bend

*Points*
:   Array of doubles (see Remarks)

#### Return Value

True if the note is a bend note, false if not

Remarks

Points will contain six (6) doubles (three (3) each for the start point and endpoint), one set for each segment in the bend line:

[  x, y, z, x, y, z ]

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)
