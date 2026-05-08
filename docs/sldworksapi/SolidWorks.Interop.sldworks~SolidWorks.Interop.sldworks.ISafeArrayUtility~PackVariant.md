# PackVariant Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PackVariant`

Packs the specified native SOLIDWORKS Dispatch-based objects of the same data type into a Variant SafeArray and returns that packed Variant SafeArray to use in methods requiring passing a packed Variant SafeArray.
Packs the specified native SOLIDWORKS Dispatch-based objects of the same data type into a Variant SafeArray and returns that packed Variant SafeArray to use in methods requiring passing a packed Variant SafeArray.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PackVariant( _
   ByRef VariantArray As System.Object, _
   ByVal Count As System.Integer, _
   ByVal Type As System.Integer, _
   ByRef Data As System.Integer _
) 
```

```

Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Count As System.Integer
Dim Type As System.Integer
Dim Data As System.Integer
 
instance.PackVariant(VariantArray, Count, Type, Data)
```

```

void PackVariant( 
   out System.object VariantArray,
   System.int Count,
   System.int Type,
   ref System.int Data
)
```

```

void PackVariant( 
   [Out] System.Object^ VariantArray,
   System.int Count,
   System.int Type,
   System.int% Data
) 
```

#### Parameters

*VariantArray*
:   Packed Variant SafeArray

*Count*
:   Number of native SOLIDWORKS Dispatch-based objects of Type

*Type*
:   Data type as defined in [swSafeArrayType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSafeArrayType_e.html)

*Data*
:   Native SOLIDWORKS Dispatch-based objects of Type

Example

[Get Scale Factor of Each Model View (C++)](Get_Scale_of_Each_Model_View_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::GetInfo Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetInfo.md)  
[ISafeArrayUtility::UnPackVariant Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~UnPackVariant.md)
