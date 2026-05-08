# IsSame Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsSame`

Gets whether the two specified objects are the same object.
Gets whether the two specified objects are the same object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsSame( _
   ByVal Object1 As System.Object, _
   ByVal Object2 As System.Object _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim Object1 As System.Object
Dim Object2 As System.Object
Dim value As System.Integer
 
value = instance.IsSame(Object1, Object2)
```

```

System.int IsSame( 
   System.object Object1,
   System.object Object2
)
```

```

System.int IsSame( 
   System.Object^ Object1,
   System.Object^ Object2
) 
```

#### Parameters

*Object1*
:   Object

*Object2*
:   Object

#### Return Value

Object equality as defined by [swObjectEquality](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swObjectEquality.html)

Example

[Compare Selected Objects and Their Persistent Reference IDs (VB.NET)](Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_VBNET.htm)  
[Compare Selected Objects and Their Persistent Reference IDs (VBA)](Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_VB.htm)  
[Compare Selected Objects and Their Persistent Reference IDs (C#)](Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[IModelDocExtension::IsSamePersistentID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsSamePersistentID.md)
