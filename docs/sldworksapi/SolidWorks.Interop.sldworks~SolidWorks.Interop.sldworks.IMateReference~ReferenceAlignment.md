# ReferenceAlignment Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceAlignment`

Gets the mate reference alignment for the specified mate reference entity in the selected mate reference.
Gets the mate reference alignment for the specified mate reference entity in the selected mate reference.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ReferenceAlignment( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As IMateReference
Dim Index As System.Integer
Dim value As System.Integer
 
value = instance.ReferenceAlignment(Index)
```

```

System.int ReferenceAlignment( 
   System.int Index
) {get;}
```

```

property System.int ReferenceAlignment {
   System.int get(System.int Index);
}
```

#### Parameters

*Index*
:   Mate reference entity as defined by [swMateReferenceIndex\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceIndex_e.html)

#### Property Value

Type of alignment as defined by [swMateReferenceAlignment\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceAlignment_e.html)

Remarks

Before calling this property, call [IMateReference::ReferenceEntityCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntityCount.md) to determine the number of mate reference entities for the mate reference.

This method returns -1 if there is no reference entity. See [IMateReference::ReferenceEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntity.md) for details.

Example

[Get Mate Reference Properties (VBA)](Get_Mate_Reference_Properties_Example_VB.htm)  
[Get Mate Reference Properties (VB.NET)](Get_Mate_Reference_Properties_Example_VBNET.htm)  
[Get Mate Reference Properties (C#)](Get_Mate_Reference_Properties_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.md)  
[IMateReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference_members.md)
