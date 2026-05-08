# PutLongLong Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutLongLong`

Adds the specified long long value to a Variant SafeArray of long long values.
Adds the specified long long value to a Variant SafeArray of long long values.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PutLongLong( _
   ByRef VariantArray As System.Object, _
   ByVal Index As System.Integer, _
   ByVal Value As System.Long _
) 
```

```

Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim Value As System.Long
 
instance.PutLongLong(VariantArray, Index, Value)
```

```

void PutLongLong( 
   out System.object VariantArray,
   System.int Index,
   System.long Value
)
```

```

void PutLongLong( 
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.int64 Value
) 
```

#### Parameters

*VariantArray*
:   Variant SafeArray of long long values

*Index*
:   Index of long long value

*Value*
:   Long long value

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::GetLongLong Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetLongLong.md)
