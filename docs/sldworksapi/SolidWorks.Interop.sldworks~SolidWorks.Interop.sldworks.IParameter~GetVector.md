# GetVector Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetVector`

Extracts information of type vector from a parameter.
Extracts information of type vector from a parameter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetVector( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
) 
```

```

Dim instance As IParameter
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
 
instance.GetVector(X, Y, Z)
```

```

void GetVector( 
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

```

void GetVector( 
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
) 
```

#### Parameters

*X*
:   x vector value stored on the parameter

*Y*
:   y vector value stored on the parameter

*Z*
:   z vector value stored on the parameter

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md)  
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.md)  
[IParameter::GetVectorVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetVectorVB.md)  
[IParameter::SetVector2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetVector2.md)
