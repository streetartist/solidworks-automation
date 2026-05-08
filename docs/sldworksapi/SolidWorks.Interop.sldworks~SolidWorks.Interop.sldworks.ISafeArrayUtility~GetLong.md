# GetLong Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetLong`

Gets the specified long value in a Variant SafeArray of long values.
Gets the specified long value in a Variant SafeArray of long values.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLong( _
   ByVal VariantArray As System.Object, _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim value As System.Integer
 
value = instance.GetLong(VariantArray, Index)
```

```

System.int GetLong( 
   System.object VariantArray,
   System.int Index
)
```

```

System.int GetLong( 
   System.Object^ VariantArray,
   System.int Index
) 
```

#### Parameters

*VariantArray*
:   Variant SafeArray of long values

*Index*
:   Index of a long value

#### Return Value

Long value

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::PutLong Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutLong.md)
