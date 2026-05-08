# GetByte Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetByte`

Gets the specified byte value in a Variant SafeArray of byte values.
Gets the specified byte value in a Variant SafeArray of byte values.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetByte( _
   ByVal VariantArray As System.Object, _
   ByVal Index As System.Integer _
) As System.Byte
```

```

Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim value As System.Byte
 
value = instance.GetByte(VariantArray, Index)
```

```

System.byte GetByte( 
   System.object VariantArray,
   System.int Index
)
```

```

System.byte GetByte( 
   System.Object^ VariantArray,
   System.int Index
) 
```

#### Parameters

*VariantArray*
:   Variant SafeArray of byte values

*Index*
:   Index of byte value

#### Return Value

Byte value

Example

[Get Object's Persistent Reference ID (C++)](Get_Object_s_Persistent_Reference_ID_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::PutByte Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutByte.md)
