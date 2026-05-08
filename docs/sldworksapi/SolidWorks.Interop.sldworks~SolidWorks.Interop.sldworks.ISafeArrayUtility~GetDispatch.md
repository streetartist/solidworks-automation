# GetDispatch Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetDispatch`

Gets the specified Dispatch object in a Variant SafeArray of Dispatch objects.
Gets the specified Dispatch object in a Variant SafeArray of Dispatch objects.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDispatch( _
   ByVal VariantArray As System.Object, _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetDispatch(VariantArray, Index)
```

```

System.object GetDispatch( 
   System.object VariantArray,
   System.int Index
)
```

```

System.Object^ GetDispatch( 
   System.Object^ VariantArray,
   System.int Index
) 
```

#### Parameters

*VariantArray*
:   Variant SafeArray of Dispatch objects

*Index*
:   Index of Dispatch object

#### Return Value

Dispatch object

Example

[Get Scale Factor of Each Model View (C++)](Get_Scale_of_Each_Model_View_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.md)  
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.md)  
[ISafeArrayUtility::PutDispatch Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutDispatch.md)
