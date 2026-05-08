# PutLong Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutLong`

Adds the specified long value to a Variant SafeArray of long values.
Adds the specified long value to a Variant SafeArray of long values.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PutLong( _
   ByRef VariantArray As System.Object, _
   ByVal Index As System.Integer, _
   ByVal Value As System.Integer _
) 
```

```

Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim Value As System.Integer
 
instance.PutLong(VariantArray, Index, Value)
```

```

void PutLong( 
   out System.object VariantArray,
   System.int Index,
   System.int Value
)
```

```

void PutLong( 
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.int Value
) 
```

#### Parameters

*VariantArray*
:   Variant SafeArray of long values

*Index*
:   Index of long value

*Value*
:   Long value

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::GetLong Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetLong.md)
