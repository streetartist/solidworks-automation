# GetExtremePoint Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetExtremePoint`

Calculates the extreme point of the model in the specified direction.
Calculates the extreme point of the model in the specified direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExtremePoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByRef Outx As System.Double, _
   ByRef Outy As System.Double, _
   ByRef Outz As System.Double _
) As System.Boolean
```

```

Dim instance As IBody2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Outx As System.Double
Dim Outy As System.Double
Dim Outz As System.Double
Dim value As System.Boolean
 
value = instance.GetExtremePoint(X, Y, Z, Outx, Outy, Outz)
```

```

System.bool GetExtremePoint( 
   System.double X,
   System.double Y,
   System.double Z,
   out System.double Outx,
   out System.double Outy,
   out System.double Outz
)
```

```

System.bool GetExtremePoint( 
   System.double X,
   System.double Y,
   System.double Z,
   [Out] System.double Outx,
   [Out] System.double Outy,
   [Out] System.double Outz
) 
```

#### Parameters

*X*
:   X component of the direction vector

*Y*
:   Y component of the direction vector

*Z*
:   Z component of the direction vector

*Outx*
:   Extreme point X coordinate

*Outy*
:   Extreme point Y coordinate

*Outz*
:   Extreme point Z coordinate

#### Return Value

True if a point was found, false if not

Remarks

This method returns the furthest possible point of intersection between a plane normal to the direction vector specified and the model as the plane moves along the direction vector. For example, if the model is a right cube centered on the origin and the direction vector is (1.0, 1.0, 1.0), then the extreme point is the vertex at (1.0,  
1.0, 1.0).

If there is more than one point (for example, if there is a face perpendicular to the direction vector), SOLIDWORKS returns a unique point that it finds in a deterministic way.

**COM example**

HRESULT auBody\_c::XDispatch2::GetExtremePoint( double x, double y, double z, double\*  
outx, double\* outy, double\* outz, VARIANT\_BOOL\* found ) {

> METHOD\_PROLOGUE\_EX\_(auBody\_c, Dispatch2)
>
> AU\_INTERFACE\_VERIFY\_NOT\_DISCONNECTED
>
> BOOL gotIt = pThis->GetExtremePoint(x, y, z, outx, outy, outz);  
> \*found = gotIt ? VARIANT\_True : VARIANT\_false;  
> return gotIt ? S\_OK : S\_false;

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
