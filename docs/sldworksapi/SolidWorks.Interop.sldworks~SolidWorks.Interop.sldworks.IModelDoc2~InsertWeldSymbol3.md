# InsertWeldSymbol3 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertWeldSymbol3`

Inserts a weld symbol into the model.
Inserts a weld symbol into the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertWeldSymbol3() As System.Object
```

```

Dim instance As IModelDoc2
Dim value As System.Object
 
value = instance.InsertWeldSymbol3()
```

```

System.object InsertWeldSymbol3()
```

```

System.Object^ InsertWeldSymbol3(); 
```

#### Return Value

Newly created [weld symbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)

Remarks

To use this method, insert the weld symbol into the model and then manipulate the properties and methods on the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md) object.

A list of weld symbol names can be found in **C:\ProgramData\SolidWorks\SolidWorks 20***nn*\**lang**\**english\gtol.sym****.** The currently supported list of ISO weld symbols is:

- BUTT
- BUSQ
- BUSV
- BUSB
- BUSVBR
- BUSBR
- BUSU
- BUSJ
- BACK
- FILL
- PLUG
- SPOT
- SEAM
- SEAMC
- JSPT
- JSM

Example

[Insert Weld Symbol Example (VBA)](Insert_Weld_Symbol_Example_VB.htm)  
[Insert Weld Symbol Example (VB.NET)](Insert_Weld_Symbol_Example_VBNET.htm)  
[Insert Weld Symbol Example (C#)](Insert_Weld_Symbol_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
