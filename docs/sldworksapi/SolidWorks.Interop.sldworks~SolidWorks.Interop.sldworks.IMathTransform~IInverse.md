# IInverse Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IInverse`

Creates a new math transform by inverting the values in an already existing math transform.
Creates a new math transform by inverting the values in an already existing math transform.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInverse() As MathTransform
```

```

Dim instance As IMathTransform
Dim value As MathTransform
 
value = instance.IInverse()
```

```

MathTransform IInverse()
```

```

MathTransform^ IInverse(); 
```

#### Return Value

[Math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) or NULL if the operation fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)  
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.md)  
[IMathTransform::Inverse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~Inverse.md)
