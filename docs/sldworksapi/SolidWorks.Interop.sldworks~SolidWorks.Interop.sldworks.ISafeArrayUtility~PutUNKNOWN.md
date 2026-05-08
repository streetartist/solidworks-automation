# PutUNKNOWN Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutUNKNOWN`

Adds the specified UNKNOWN object to a Variant SafeArray of UNKNOWN objects.
Adds the specified UNKNOWN object to a Variant SafeArray of UNKNOWN objects.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PutUNKNOWN( _
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
 
instance.PutUNKNOWN(VariantArray, Index, Value)
```

```

void PutUNKNOWN( 
   out System.object VariantArray,
   System.int Index,
   System.object Value
)
```

```

void PutUNKNOWN( 
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.Object^ Value
) 
```

#### Parameters

*VariantArray*
:   Variant SafeArray of UNKNOWN objects

*Index*
:   Index of UNKNOWN object

*Value*
:   UNKNOWN object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::GetUNKNOWN Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetUNKNOWN.md)
