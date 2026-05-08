# CheckSpelling Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~CheckSpelling`

Spell checks the text in this annotation.
Spell checks the text in this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CheckSpelling( _
   ByVal Options As System.Integer, _
   ByVal Dictionary As System.String _
) As System.Object
```

```

Dim instance As IAnnotation
Dim Options As System.Integer
Dim Dictionary As System.String
Dim value As System.Object
 
value = instance.CheckSpelling(Options, Dictionary)
```

```

System.object CheckSpelling( 
   System.int Options,
   System.string Dictionary
)
```

```

System.Object^ CheckSpelling( 
   System.int Options,
   System.String^ Dictionary
) 
```

#### Parameters

*Options*
:   Spell-check options as defined in [swCheckSpellingOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCheckSpellingOptions_e.html)

*Dictionary*
:   :   Full path and filename of user dictionary to use (see **Remarks**)

#### Return Value

Array of the misspelled words in this annotation

Remarks

The SOLIDWORKS spell checker always uses a main dictionary, which is language specific. Use the Dictionary argument to specify an additional dictionary. If Dictionary is left blank, then no additional user dictionary is used.

You can also specify additional custom dictionaries by adding them in the appropriate location in the SOLIDWORKS registry.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)
