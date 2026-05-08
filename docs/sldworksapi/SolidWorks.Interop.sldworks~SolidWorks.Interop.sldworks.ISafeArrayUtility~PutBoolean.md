# PutBoolean Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutBoolean`

Adds the specified Boolean value to a Variant SafeArray of Boolean values.
Adds the specified Boolean value to a Variant SafeArray of Boolean values.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PutBoolean( _
   ByRef VariantArray As System.Object, _
   ByVal Index As System.Integer, _
   ByVal Value As System.Boolean _
) 
```

```

Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim Value As System.Boolean
 
instance.PutBoolean(VariantArray, Index, Value)
```

```

void PutBoolean( 
   out System.object VariantArray,
   System.int Index,
   System.bool Value
)
```

```

void PutBoolean( 
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.bool Value
) 
```

#### Parameters

*VariantArray*
:   Variant SafeArray of Boolean values

*Index*
:   Index of Boolean value

*Value*
:   Boolean value

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::GetBoolean Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetBoolean.md)
