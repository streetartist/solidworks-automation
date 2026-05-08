# Next Method (IEnumDocuments2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2~Next`

Gets the next document in the documents enumeration.
Gets the next document in the documents enumeration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Next( _
   ByVal Celt As System.Integer, _
   ByRef Rgelt As ModelDoc2, _
   ByRef PceltFetched As System.Integer _
) 
```

```

Dim instance As IEnumDocuments2
Dim Celt As System.Integer
Dim Rgelt As ModelDoc2
Dim PceltFetched As System.Integer
 
instance.Next(Celt, Rgelt, PceltFetched)
```

```

void Next( 
   System.int Celt,
   out ModelDoc2 Rgelt,
   out System.int PceltFetched
)
```

```

void Next( 
   System.int Celt,
   [Out] ModelDoc2^ Rgelt,
   [Out] System.int PceltFetched
) 
```

#### Parameters

*Celt*
:   Number of documents for the documents enumeration

*Rgelt*
:   Pointer to an array of [documents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) of size Celt

*PceltFetched*
:   Pointer to the number of documents returned from the list; this value can be less than Celt if you ask for more documents than exist, or it can be NULL if no more documents exist.

Remarks

For use in in-process DLLs only.

Example

[Get List of Open Documents (C++)](Get_List_of_Open_Documents_Example_CPlusPlus_COM.htm)  
[Traverse All Open Documents (C++)](Traverse_All_Open_Documents_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnumDocuments2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2.md)  
[IEnumDocuments2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2_members.md)
