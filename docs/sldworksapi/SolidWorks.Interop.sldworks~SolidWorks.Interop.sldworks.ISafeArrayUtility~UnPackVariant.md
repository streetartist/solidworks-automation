# UnPackVariant Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~UnPackVariant`

Unpacks the specified packed Variant SafeArray to native SOLIDWORKS Dispatch-based objects of the same data type.
Unpacks the specified packed Variant SafeArray to native SOLIDWORKS Dispatch-based objects of the same data type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UnPackVariant( _
   ByVal VariantArray As System.Object, _
   ByVal Count As System.Integer _
) As System.Integer
```

```

Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Count As System.Integer
Dim value As System.Integer
 
value = instance.UnPackVariant(VariantArray, Count)
```

```

System.int UnPackVariant( 
   System.object VariantArray,
   System.int Count
)
```

```

System.int UnPackVariant( 
   System.Object^ VariantArray,
   System.int Count
) 
```

#### Parameters

*VariantArray*
:   Variant SafeArray

*Count*
:   Number of native SOLIDWORKS Dispatch-based objects of the same data type

#### Return Value

Native SOLIDWORKS Dispatch-based objects of the same data type

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::GetInfo Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetInfo.md)  
[ISafeArrayUtility::PackVariant Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PackVariant.md)
