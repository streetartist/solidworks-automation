# GetBendLineValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBendLineValues`

Obsolete. Superseded by INote::GetBendLineValues2.
Obsolete. Superseded by [INote::GetBendLineValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBendLineValues2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBendLineValues( _
   ByRef Up As System.Boolean, _
   ByRef Angle As System.Double, _
   ByRef Radius As System.Double, _
   ByRef StartPt As MathPoint, _
   ByRef EndPt As MathPoint _
) As System.Boolean
```

```

Dim instance As INote
Dim Up As System.Boolean
Dim Angle As System.Double
Dim Radius As System.Double
Dim StartPt As MathPoint
Dim EndPt As MathPoint
Dim value As System.Boolean
 
value = instance.GetBendLineValues(Up, Angle, Radius, StartPt, EndPt)
```

```

System.bool GetBendLineValues( 
   out System.bool Up,
   out System.double Angle,
   out System.double Radius,
   out MathPoint StartPt,
   out MathPoint EndPt
)
```

```

System.bool GetBendLineValues( 
   [Out] System.bool Up,
   [Out] System.double Angle,
   [Out] System.double Radius,
   [Out] MathPoint^ StartPt,
   [Out] MathPoint^ EndPt
) 
```

#### Parameters

*Up*
:   True if the bend is up, false if the bend is down

*Angle*
:   Angle of the bend

*Radius*
:   Radius of the bend

*StartPt*
:   Start [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) of the bend line

*EndPt*
:   End [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) of the bend line

#### Return Value

True if the note is a bend note, false if not

Example

[Get Bend Line Note Values (VBA)](Get_Bend_Line_Note_Values_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::IsBendLineNote Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsBendLineNote.md)
