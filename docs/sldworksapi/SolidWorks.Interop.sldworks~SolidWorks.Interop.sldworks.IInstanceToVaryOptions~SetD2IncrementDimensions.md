# SetD2IncrementDimensions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~SetD2IncrementDimensions`

Sets the dimensions to increment in Direction 2.
Sets the dimensions to increment in Direction 2.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetD2IncrementDimensions( _
   ByVal IncrementDimensions As System.Object, _
   ByVal IncrementDimValues As System.Object _
) As System.Boolean
```

```

Dim instance As IInstanceToVaryOptions
Dim IncrementDimensions As System.Object
Dim IncrementDimValues As System.Object
Dim value As System.Boolean
 
value = instance.SetD2IncrementDimensions(IncrementDimensions, IncrementDimValues)
```

```

System.bool SetD2IncrementDimensions( 
   System.object IncrementDimensions,
   System.object IncrementDimValues
)
```

```

System.bool SetD2IncrementDimensions( 
   System.Object^ IncrementDimensions,
   System.Object^ IncrementDimValues
) 
```

#### Parameters

*IncrementDimensions*
:   Array of dimensions to increment

*IncrementDimValues*
:   Array of dimension increments in Direction 2

#### Return Value

True if the dimensions are incremented successfully, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IInstanceToVaryOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.md)  
[IInstanceToVaryOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions_members.md)
