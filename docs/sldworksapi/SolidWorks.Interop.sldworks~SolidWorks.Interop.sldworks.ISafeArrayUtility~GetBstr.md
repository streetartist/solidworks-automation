# GetBstr Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetBstr`

Gets the specified BSTR in a Variant SafeArray of BSTRs.
Gets the specified BSTR in a Variant SafeArray of BSTRs.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBstr( _
   ByVal VariantArray As System.Object, _
   ByVal Index As System.Integer _
) As System.String
```

```

Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim value As System.String
 
value = instance.GetBstr(VariantArray, Index)
```

```

System.string GetBstr( 
   System.object VariantArray,
   System.int Index
)
```

```

System.String^ GetBstr( 
   System.Object^ VariantArray,
   System.int Index
) 
```

#### Parameters

*VariantArray*
:   Variant SafeArray of BSTRs

*Index*
:   Index of BSTR

#### Return Value

BSTR

Remarks

Example

[Get Names of Configurations Using Variant (C++)](ConfigurationTraversalCPP.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::PutBstr Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutBstr.md)
