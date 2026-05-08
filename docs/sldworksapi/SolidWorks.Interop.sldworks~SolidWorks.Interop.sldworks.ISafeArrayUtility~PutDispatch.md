# PutDispatch Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutDispatch`

Adds the specified Dispatch object to a Variant SafeArray of Dispatch objects.
Adds the specified Dispatch object to a Variant SafeArray of Dispatch objects.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PutDispatch( _
   ByRef VariantArray As System.Object, _
   ByVal Index As System.Integer, _
   ByVal Value As System.Object _
) 
```

```

Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim Value As System.Object
 
instance.PutDispatch(VariantArray, Index, Value)
```

```

void PutDispatch( 
   out System.object VariantArray,
   System.int Index,
   System.object Value
)
```

```

void PutDispatch( 
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.Object^ Value
) 
```

#### Parameters

*VariantArray*
:   Variant SafeArray of Dispatch objects

*Index*
:   Index of Dispatch object

*Value*
:   Dispatch object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::GetDispatch Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetDispatch.md)
