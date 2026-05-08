# PutBstr Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutBstr`

Adds the specified BSTR to a Variant SafeArray of BSTRs.
Adds the specified BSTR to a Variant SafeArray of BSTRs.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PutBstr( _
   ByRef VariantArray As System.Object, _
   ByVal Index As System.Integer, _
   ByVal Value As System.String _
) 
```

```

Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim Value As System.String
 
instance.PutBstr(VariantArray, Index, Value)
```

```

void PutBstr( 
   out System.object VariantArray,
   System.int Index,
   System.string Value
)
```

```

void PutBstr( 
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.String^ Value
) 
```

#### Parameters

*VariantArray*
:   Variant SafeArray of BSTRs

*Index*
:   Index of BSTR

*Value*
:   BSTR

Remarks

Be aware that calling ISafeArrayUtility::PutBstr within a loop that inserts a BSTR repeatedly declared on the stack results in an array of pointers to the same BSTR; i.e., all elements of the SafeArray are the same, which is most likely not your intention. For example, you should avoid using code similar to the following:

for (ULONG ulIndex = 0L; ulIndex < ulSize; ulIndex++)  
{   
    CString testString;  
    testString.Format(\_T('Index = %d'), ulIndex);  
    CComBSTR bstrTemp = testString;  
    HRESULT hres = iSAUtil->PutBstr(&vPacked, ulIndex, bstrTemp);

    bstrArray[ulIndex] = bstrTemp;  
}

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::GetBstr Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetBstr.md)
