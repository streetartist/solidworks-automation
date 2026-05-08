# GetUNKNOWN Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetUNKNOWN`

Gets the specified UNKNOWN object in a Variant SafeArray of UNKNOWN objects.
Gets the specified UNKNOWN object in a Variant SafeArray of UNKNOWN objects.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUNKNOWN( _
   ByVal VariantArray As System.Object, _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetUNKNOWN(VariantArray, Index)
```

```

System.object GetUNKNOWN( 
   System.object VariantArray,
   System.int Index
)
```

```

System.Object^ GetUNKNOWN( 
   System.Object^ VariantArray,
   System.int Index
) 
```

#### Parameters

*VariantArray*
:   Variant SafeArray of UNKNOWN objects

*Index*
:   Index of UNKNOWN object

#### Return Value

UNKNOWN object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::PutUNKNOWN Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutUNKNOWN.md)
