# GetInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetInfo`

Gets the number of elements in a Variant SafeArray and their data type.
Gets the number of elements in a Variant SafeArray and their data type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetInfo( _
   ByVal VariantArray As System.Object, _
   ByRef Count As System.Integer, _
   ByRef Type As System.Integer _
) 
```

```

Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Count As System.Integer
Dim Type As System.Integer
 
instance.GetInfo(VariantArray, Count, Type)
```

```

void GetInfo( 
   System.object VariantArray,
   out System.int Count,
   out System.int Type
)
```

```

void GetInfo( 
   System.Object^ VariantArray,
   [Out] System.int Count,
   [Out] System.int Type
) 
```

#### Parameters

*VariantArray*
:   Variant SafeArray

*Count*
:   Number of elements in VariantArray

*Type*
:   Data type of elements in VariantArray as defined in [swSafeArrayType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSafeArrayType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::PackVariant Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PackVariant.md)  
[ISafeArrayUtility::UnPackVariant Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~UnPackVariant.md)
