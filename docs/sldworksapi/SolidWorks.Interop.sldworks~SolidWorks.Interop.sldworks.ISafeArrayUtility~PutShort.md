# PutShort Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutShort`

Adds the specified short value to a Variant SafeArray of short values.
Adds the specified short value to a Variant SafeArray of short values.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PutShort( _
   ByRef VariantArray As System.Object, _
   ByVal Index As System.Integer, _
   ByVal Value As System.Short _
) 
```

```

Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim Value As System.Short
 
instance.PutShort(VariantArray, Index, Value)
```

```

void PutShort( 
   out System.object VariantArray,
   System.int Index,
   System.short Value
)
```

```

void PutShort( 
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.short Value
) 
```

#### Parameters

*VariantArray*
:   Variant SafeArray of short values

*Index*
:   Index of short value

*Value*
:   Short value

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::GetShort Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetShort.md)
