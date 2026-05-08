# GetBoolean Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetBoolean`

Gets the specified Boolean value in a Variant SafeArray of Boolean values.
Gets the specified Boolean value in a Variant SafeArray of Boolean values.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBoolean( _
   ByVal VariantArray As System.Object, _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim value As System.Boolean
 
value = instance.GetBoolean(VariantArray, Index)
```

```

System.bool GetBoolean( 
   System.object VariantArray,
   System.int Index
)
```

```

System.bool GetBoolean( 
   System.Object^ VariantArray,
   System.int Index
) 
```

#### Parameters

*VariantArray*
:   Variant SafeArray of Boolean values

*Index*
:   Index of Boolean value

#### Return Value

Boolean value

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::PutBoolean Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutBoolean.md)
