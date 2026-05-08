# AllowFailedFeatureCreation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AllowFailedFeatureCreation`

Sets whether to allow the creation of a feature that has rebuild errors.
Sets whether to allow the creation of a feature that has rebuild errors.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AllowFailedFeatureCreation( _
   ByVal YesNo As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim YesNo As System.Boolean
Dim value As System.Boolean
 
value = instance.AllowFailedFeatureCreation(YesNo)
```

```

System.bool AllowFailedFeatureCreation( 
   System.bool YesNo
)
```

```

System.bool AllowFailedFeatureCreation( 
   System.bool YesNo
) 
```

#### Parameters

*YesNo*
:   True if features are to be created regardless of rebuild errors, false if not

#### Return Value

The previous value, which is now replaced by the value for YesNo

Remarks

By default, features are not created when invalid geometry is specified; however, after calling this method with YesNo set to True, the features are created but with rebuild errors.

Example

[Create Feature With Invalid Geometry (VBA)](Create_Feature_with_Invalid_Geometry_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
